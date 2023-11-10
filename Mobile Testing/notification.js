import React, {useState, useEffect} from 'react';
import {Text, Button, SafeAreaView} from 'react-native';
import {SafeAreaProvider} from 'react-native-safe-area-context';
import notifee, {
  AuthorizationStatus,
  AndroidImportance,
  EventType,
} from '@notifee/react-native';

const CHANNEL_ID = 'custom';

const App = () => {
  const [loading, setLoading] = useState(true);
  const [permitted, setPermitted] = useState(false);

  // Detects how app was launched
  async function bootstrap() {
    const initialNotification = await notifee.getInitialNotification();

    if (initialNotification) {
      console.log(
        'Notification caused application to open',
        initialNotification.notification,
      );
      console.log(
        'Press action used to open the app',
        initialNotification.pressAction,
      );
    }
  }

  useEffect(() => {
    bootstrap().then(() => setLoading(false));
    // .catch(console.error);
  }, []);

  // Handlers for 2 events: app in foreground and app in background
  useEffect(() => {
    return notifee.onForegroundEvent(({type, detail}) => {
      switch (type) {
        case EventType.DISMISSED:
          console.log('User dismissed notification', detail.notification);
          break;
        case EventType.PRESS:
          console.log('User pressed notification', detail.notification);
          break;
      }
    });
  }, []);

  notifee.onBackgroundEvent(async ({type, detail}) => {
    const {notification, pressAction} = detail;

    // Check if the user pressed the "Mark as read" action
    if (type === EventType.ACTION_PRESS && pressAction.id === 'mark-as-read') {
      // Update external API
      console.log('User marked as read');
      await fetch(`https://my-api.com/chat/${notification.data.chatId}/read`, {
        method: 'POST',
      });

      // Remove the notification
      await notifee.cancelNotification(notification.id);
    }
  });

  if (loading) {
    return null;
  }

  // Callback from button to demonstrate how to generate a notification
  function onDisplayNotification() {
    notifee.requestPermission().then(permissionResult => {
      if (permissionResult.authorizationStatus === AuthorizationStatus.DENIED) {
        console.log('User denied permissions request');
      } else if (
        permissionResult.authorizationStatus === AuthorizationStatus.AUTHORIZED
      ) {
        setPermitted(true);
        console.log('User granted permissions request');
      } else if (
        permissionResult.authorizationStatus === AuthorizationStatus.PROVISIONAL
      ) {
        setPermitted(true);
        console.log('User provisionally granted permissions request');
      }
    });

    if (!permitted) {
      console.log('Permissions not granted');
      return;
    }

    // Create a channel (required for Android)
    notifee.createChannel({
      id: CHANNEL_ID,
      name: 'Banana Channel',
      // Must be "HIGH" to cause notification to show over apps on Android
      importance: AndroidImportance.HIGH,
    });

    notifee.displayNotification({
      title: 'The Batman - Part 2',
      body: 'NEWS - Filming To Begin Soon!',
      // icon, sound, vibration, etc. are optional
      android: {
        channelId: CHANNEL_ID,
        // necessary here for old Android versions
        importance: AndroidImportance.HIGH,

        // pressAction is needed if you want the notification to open the app when pressed
        pressAction: {
          id: 'default',
        },
      },
    });
  }

  return (
    <SafeAreaProvider>
      <SafeAreaView>
        <Text>Hello World</Text>
        <Button
          title="Press console log me"
          onPress={() => console.error('huh')}
        />
        <Button title="Do It!" onPress={() => onDisplayNotification()} />
      </SafeAreaView>
    </SafeAreaProvider>
  );
};

export default App;
