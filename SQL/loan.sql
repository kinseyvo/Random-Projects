-- loan: loan_no, loan_amt
-- borrower: loan_no*, brwr_no*, brwr_name, income
-- 1-to-Many relationship for loan_no

-- Write an SQL query that will list all loans and the number of borrowers per loan
SELECT loan_no, COUNT(brwr_no) AS number_of_borrowers
FROM loan
GROUP BY loan_no
HAVING COUNT(brwr_no) > 1;
