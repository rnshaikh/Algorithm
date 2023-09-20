-- https://www.w3resource.com/sql-exercises/sql-joins-exercises.php#SQLEDITOR


-- 1. From the following tables write a SQL query to find the salesperson and customer who reside in the same city. 
-- Return Salesman, cust_name and city.
select S.name as salesman, C.cust_name as customer_name, S.city from salesman as S 
inner join customer as C on S.salesman_id = C.salesman_id where S.city = c.city;


---2.  From the following tables write a SQL query to find those orders where the order amount exists between 500 and 2000. 
-- Return ord_no, purch_amt, cust_name, city
select O.ord_no, O.purch_amt, C.cust_name, C.city from orders as O inner join customer as C on 
O.customer_id = C.customer_id where O.purch_amt Between 500 and 2000;


/*
From the following tables write a SQL query to find the salesperson(s) and the customer(s) he represents. 
Return Customer Name, city, Salesman, commission
 */
select C.cust_name as "Customer Name", C.city, S.name as Salesman, S.commission from 
customer as C  inner join salesman as S on C.salesman_id = S.salesman_id;

/* 
From the following tables write a SQL query to find salespeople who received commissions of more than 12 percent from the company. 
Return Customer Name, customer city, Salesman, commission.
*/
select C.cust_name as "Customer Name", C.city as "customer_city", S.name as Salesman, S.commission from 
customer as C  inner join salesman as S on C.salesman_id = S.salesman_id where S.commission > 0.12


/*
From the following tables write a SQL query to locate those salespeople 
who do not live in the same city where their customers live and have received a commission of more than 12% from the company. 
Return Customer Name, customer city, Salesman, salesman city, commission
*/

select C.cust_name as "Customer Name", C.city as "customer_city", S.name as Salesman, S.city as "salesman city" ,S.commission from 
customer as C  inner join salesman as S on C.salesman_id = S.salesman_id where S.commission > 0.12 and C.city != S.city

/*
     From the following tables write a SQL query to find the details of an order. 
     Return ord_no, ord_date, purch_amt, Customer Name, grade, Salesman, commission
*/

select O.ord_no, O.ord_date, O.purch_amt, C.cust_name as "Customer Name", C.grade, S.name as salesman, S.commission from orders as O 
inner join customer as C on O.customer_id  = C.customer_id
inner join salesman as S on O.salesman_id = S.salesman_id;

/* 
Write a SQL statement to join the tables salesman, 
customer and orders so that the same column of each table appears once and only the relational rows are returned
*/

SELECT * 
FROM orders 
NATURAL JOIN customer  
NATURAL JOIN salesman;


/*
From the following tables write a SQL query to find those customers with a grade less than 300. 
Return cust_name, customer city, grade, Salesman,salesmancity. 
The result should be ordered by ascending customer_id.  
*/

select C.cust_name as "Customer Name", C.city as "customer_city", S.name as Salesman, S.city as "salesman city" ,S.commission from 
customer as C  inner join salesman as S on C.salesman_id = S.salesman_id order by C.customer_id


/*
Write a SQL statement to make a report with customer name, city, order number, order date, 
and order amount in ascending order according to the order date to determine whether any of the existing customers have placed an order or not
*/

select O.ord_no, O.ord_date, O.purch_amt as "order amount", 
C.cust_name as "customer name", 
C.city 
from orders as O left join customer as C on 
C.customer_id = O.customer_id order by O.ord_date


/*
SQL statement to generate a report with customer name, city, order number, order date, order amount, 
salesperson name, and commission to determine 
if any of the existing customers have not placed orders or if they have placed orders through their salesman or by themselves
*/
select O.ord_date, O.purch_amt as "order amount", 
C.cust_name as "customer name", 
C.city, S.name as "salesperson name", S.commission
 
from orders as O left join customer as C on 
C.customer_id = O.customer_id 
left join salesman as S on 
C.salesman_id = S.salesman_id

order by O.ord_date

/* 
 Write a SQL statement to generate a list in ascending order of salespersons 
 who work either for one or more customers or have not yet joined any of the customers

*/

select S.name as "salesperson name"
from salesman as S left join customer as C on 
S.salesman_id = C.salesman_id
order by S.salesman_id

/* 
Write a SQL statement to generate a list of all the salesmen who either work for one or more customers or have yet to join any of them. The customer may have placed one or more orders at 
or above order amount 2000, and must have a grade, or he may not have placed any orders to the associated supplier.

*/


SELECT C.cust_name, C.city , C.grade, 
S.name AS "Salesman", 
O.ord_no, O.ord_date, O.purch_amt 
FROM customer C 
LEFT JOIN salesman S 
ON S.salesman_id = C.salesman_id
LEFT JOIN orders O
ON C.customer_id = O.customer_id 
WHERE 
(O.purch_amt>=2000 AND C.grade IS NOT NULL);



/* 
Write a SQL statement to generate a report with the customer name, city, order no. 
order date, purchase amount for only those customers on the list 
who must have a grade and placed one or more orders or which order(s) 
have been placed by the customer who neither is on the list nor has a grade. 
*/
SELECT C.cust_name, C.city , C.grade, 
O.ord_no, O.ord_date, O.purch_amt 
FROM customer C 
FULL JOIN orders O
ON C.customer_id = O.customer_id 
WHERE 
(C.grade IS NOT NULL);



/*
Write a SQL query to combine each row of the salesman table with each row of the customer table.

*/

SELECT * 
FROM salesman a 
CROSS JOIN customer b;


/*
Write a SQL statement to create a Cartesian product between salesperson and customer, 
i.e. each salesperson will appear for all customers and vice versa for that salesperson who belongs to that city.  
*/

SELECT * 
FROM customer C
CROSS JOIN salesman S;



/*
From the following 
tables write a SQL query to select all rows from both participating 
tables as long as there is a match between pro_com and com_id. 
*/
SELECT * 
FROM company_mast C
FULL JOIN item_mast S on C.COM_ID = s.PRO_COM;


/*
Write a SQL query to display the item name, price, and company name of all the products. 
*/

SELECT * 
FROM item_mast C
JOIN company_mast S on C.PRO_COM= S.COM_ID;


/*
From the following tables write a SQL query to calculate and find the 
average price of items of each company higher than or equal to Rs. 350. Return average value and company name. 
*/

SELECT FORMAT(AVG(C.PRO_PRICE),2) as avg_price, S.com_name as company_name
FROM item_mast C JOIN company_mast S on C.PRO_COM = S.COM_ID
GROUP BY company_name 
having AVG(C.PRO_PRICE) >= 350



/*
 From the following tables write a SQL query to find the most expensive product of each company. 
 Return pro_name, pro_price and com_name
*/


SELECT A.pro_name, A.pro_price, F.com_name
   FROM item_mast A INNER JOIN company_mast F
   ON A.pro_com = F.com_id
     AND A.pro_price =
     (
       SELECT MAX(A.pro_price)
         FROM item_mast A
         WHERE A.pro_com = F.com_id
     );

/*
 From the following tables write a SQL query to display all the data of employees including their department.
*/

SELECT * from emp_details join emp_department on emp_details.EMP_DEPT = emp_department.DPT_CODE 



/*
 From the following tables write a SQL query to display the first and last names of each employee, 
 as well as the department name and sanction amount.
*/
SELECT emp_details.emp_fname AS "First Name", emp_lname AS "Last Name", 
    emp_department.dpt_name AS "Department", 
     dpt_allotment AS "Amount Allotted"
       FROM emp_details 
         INNER JOIN emp_department
           ON emp_details.emp_dept = emp_department.dpt_code;

/*
 From the following tables write a SQL query to find the departments with budgets 
 more than Rs. 50000 and display the first name and last name of employees
*/
SELECT emp_details.emp_fname AS "First Name", emp_lname AS "Last Name"
  FROM emp_details 
    INNER JOIN emp_department
        ON emp_details.emp_dept = emp_department.dpt_code
    AND emp_department.dpt_allotment > 50000;



/*
 From the following tables write a SQL query to find the names of departments 
 where more than two employees are employed. Return dpt_name.
*/
SELECT emp_department.dpt_name, COUNT(emp_details.EMP_IDNO ) as emp_count
  FROM emp_details 
     INNER JOIN emp_department
       ON emp_dept =dpt_code
        GROUP BY emp_department.dpt_name
          HAVING COUNT(emp_details.EMP_IDNO ) > 2;



/* Aggregation */

/*
 From the following table, write a SQL query to find the highest grade of the customers in each city. Return city, maximum grade. 
*/

select max(grade) AS "maximum grade", city from customer group by city;


/*
select max(purch_amt) AS "maximum purchase amount", customer_id from orders group by customer_id;
*/

select max(purch_amt) AS "maximum purchase amount", customer_id from orders group by customer_id;


/*
From the following table, write a SQL query to find the highest purchase amount ordered by each customer on a particular date. 
Return, order date and highest purchase amount.
*/
select max(purch_amt) AS "maximum purchase amount", ord_date, customer_id  from orders group by (ord_date, customer_id);


/*
From the following table, write a SQL query to determine the highest purchase amount made 
by each salesperson on '2012-08-17'. Return salesperson ID, purchase amount 
*/
select max(purch_amt) AS "maximum purchase amount", salesman_id from orders  WHERE ord_date = '2012-08-17' group by salesman_id;


/*
From the following table, write a SQL query to find the highest order (purchase) amount by each customer on a particular order date. 
Filter the result by highest order (purchase) amount above 2000.00. Return customer id, order date and maximum purchase amount. 
*/
select max(purch_amt) AS "maximum purchase amount", ord_date, customer_id  
from orders group by (ord_date, customer_id) having max(purch_amt)>2000.00

/*
From the following table, write a SQL query to find the maximum order (purchase) amount in 
the range 2000 - 6000 (Begin and end values are included.) 
by combination of each customer and order date. Return customer id, order date and maximum purchase amount
*/
select max(purch_amt) AS "maximum purchase amount", ord_date, customer_id  
from orders group by (ord_date, customer_id) having max(purch_amt) between 2000 and 6000




/*
SUBQURIES
*/

/*
 From the following tables, write a SQL query 
 to find all the orders issued by the salesman 'Paul Adam'. 
 Return ord_no, purch_amt, ord_date, customer_id and salesman_id.
*/
select O.ord_no, O.purch_amt, O.ord_date, O.customer_id, O.salesman_id
from Orders O Join Salesman S on O.salesman_id  = S.salesman_id where S.name = 'Paul Adam'


/*
From the following tables write a SQL query to find all orders generated by London-based salespeople. 
Return ord_no, purch_amt, ord_date, customer_id, salesman_id
*/

select * 
from Orders
where salesman_id in (select salesman_id from Salesman where city='London'); 


/*
   From the following tables write a SQL query to find all orders generated by the salespeople who may work 
   for customers whose id is 3007. Return ord_no, purch_amt, ord_date, customer_id, salesman_id. 
*/

select * 
from Orders
where salesman_id in (select salesman_id from Orders where customer_id=3007);



/*
 From the following tables write a SQL query to count the number of customers 
 with grades above the average in New York City. Return grade and count.
*/
select grade, count(*) from Customer where grade > (select AVG(grade) as grade from Customer where city='New York')
group by (grade) 


/*
 From the following tables, 
 write a SQL query to find those salespeople who earned the maximum commission. 
 Return ord_no, purch_amt, ord_date, and salesman_id.
*/

select Orders.* from Orders 
join salesman on Orders.salesman_id = salesman.salesman_id
where salesman.commission * Orders.purch_amt = (select Max(Orders.purch_amt*salesman.commission) from Orders join salesman on Orders.salesman_id = salesman.salesman_id )


/*
From the following tables write SQL query to find the customers 
who placed orders on 17th August 2012. 
Return ord_no, purch_amt, ord_date, customer_id, salesman_id and cust_name
*/
select Orders.*, Customer.cust_name from Orders 
join Customer on Orders.customer_id = Customer.customer_id
where Orders.ord_date = '2012-08-17'


/*
From the following tables write a SQL query to 
find salespeople who had more than one customer. Return salesman_id and name.
*/

select * from salesman where 1 < (select count(*) from Customer where salesman_id=salesman.salesman_id )



/*
 From the following tables write a SQL query to find those orders, which are higher than the average amount of the orders. 
 Return ord_no, purch_amt, ord_date, customer_id and salesman_id. 
*/

SELECT * 
FROM orders a
WHERE purch_amt >
    (SELECT AVG(purch_amt) FROM orders b 
     WHERE b.customer_id = a.customer_id);


/*
Write a query to find the sums of the amounts from the orders table, grouped by date, and eliminate all dates 
where the sum was not at least 1000.00 above the maximum order amount for that date
*/

SELECT sum(purch_amt) 
FROM orders a group by ord_date having sum(purch_amt) > ( 
select 1000+Max(purch_amt) from Orders b where a.ord_date = b.ord_date)


/*
Write a query to extract all data from the customer table if and 
only if one or more of the customers in the customer table are located in London. 
*/

select * from Customer where (select count(*) from Customer where city = 'New York') > 1


/*
From the following tables write a SQL query to find salespeople who deal with multiple customers. 
Return salesman_id, name, city and commission. 
*/

select * from  salesman a where ( select count(*) from Customer b where a.salesman_id = b.salesman_id) > 1



/*
From the following tables, write a SQL query to find the salespeople 
who deal the customers with more than one order. Return salesman_id, name, city and commission.
*/
select * from  salesman a where Exists (select * from Orders b where a.salesman_id = b.salesman_id and  1 < (select Count(*) from Orders C where b.customer_id = c.customer_id))



/*
From the following tables write a SQL query to find the salespeople who deal with those customers 
who live in the same city. Return salesman_id, name, city and commission. 
*/

select * from  salesman a where Exists (select * from Customer b where a.city = b.city)


/*
From the following tables write a SQL query to find salespeople whose place of residence matches any 
city where customers live. Return salesman_id, name, city and commission.
*/
SELECT *
FROM salesman 
WHERE city IN
    (SELECT city
     FROM customer);



/*
From the following tables write a SQL query to find all those salespeople whose names appear 
alphabetically lower than the customer’s name. Return salesman_id, name, city, commission.
*/

select * from  salesman a where Exists (select cust_name from Customer b where a.name < b.cust_name)


/*
From the following table write a SQL query to find all those customers with a higher grade than all the customers alphabetically 
below the city of New York. Return customer_id, cust_name, city, grade, salesman_id.
*/

SELECT *
FROM customer
WHERE grade > ANY
   (SELECT grade
	FROM CUSTOMER
	WHERE  city < 'New York');

/*
 From the following table write a SQL query to find all those orders whose order 
 amount exceeds at least one of the orders placed on September 10th 2012. 
 Return ord_no, purch_amt, ord_date, customer_id and salesman_id. 
*/

SELECT *
FROM Orders
WHERE purch_amt > ANY
   (SELECT purch_amt
	FROM orders
	WHERE  ord_date='2012/09/10');


/*
 From the following tables write a SQL query to find those orders where every order amount is less than 
 the maximum order amount of a customer who lives in London City. 
 Return ord_no, purch_amt, ord_date, customer_id and salesman_id.  
*/

SELECT *
FROM Orders a
WHERE purch_amt < 
   (SELECT max(b.purch_amt)
   FROM Orders b
   join Customer c on c.customer_id = b.customer_id
   WHERE c.city ='London'
  );


/*
 From the following tables write a SQL query to find those customers whose 
 grades are higher than those living in New York City. Return customer_id, cust_name, city, grade and salesman_id.
*/

SELECT *
FROM Customer a
WHERE grade > 
   ALL(SELECT grade
    FROM Customer b
    WHERE b.city ='New York'
  );

/*
From the following tables write a SQL query to calculate the total order amount generated by a salesperson. 
Salespersons should be from the cities where the customers reside. 
Return salesperson name, city and total order amoun

*/

SELECT *, subquery.total_amt
FROM  salesman a, (select sum(purch_amt) as total_amt, salesman_id from Orders b group by salesman_id) subquery 
where subquery.salesman_id = a.salesman_id and a.city in (select DISTINCT city from Customer)



/*
 From the following tables write a SQL query to find those customers whose grades are not the same as those who live in London City. 
 Return customer_id, cust_name, city, grade and salesman_id.
*/

SELECT * 
From Customer
where grade not in (select grade from Customer where city='London' and NOT grade IS NULL)


/*
From the following tables write a SQL query to find all those customers who have different grades than any customer who lives in Dallas City. 
Return customer_id, cust_name,city, grade and salesman_id. 
*/

SELECT * 
From Customer
where Not grade = ANY(select grade from Customer where city='Dallas')


/*
From the following tables write a 
SQL query to calculate the average price of each manufacturer's product of 350 or more. Return Average Price and Company.
*/

SELECT AVG(pro_price) AS "Average Price", 
   company_mast.com_name AS "Company"
      FROM item_mast, company_mast
         WHERE item_mast.pro_com= company_mast.com_id
           GROUP BY company_mast.com_name
   HAVING AVG(pro_price) >= 350;

/*
. From the following tables, write a SQL query to find the most expensive product of each company. 
Return Product Name, Price and Company.
*/

SELECT MAX(pro_price) AS "MAX Price", 
   company_mast.com_name AS "Company"
      FROM item_mast, company_mast
         WHERE item_mast.pro_com= company_mast.com_id
           GROUP BY company_mast.com_name

/*
 From the following tables write a SQL query to find the departments whose 
 sanction amount is higher than the average sanction amount for all departments. Return dpt_code, dpt_name and dpt_allotment.
*/
SELECT *
  FROM emp_department
  WHERE dpt_allotment >
  (
    SELECT AVG(dpt_allotment)
    FROM emp_department
  );

/*
From the following tables write a SQL query to find which departments have more than two employees. Return dpt_name.
*/

SELECT dpt_name FROM emp_department
  WHERE dpt_code IN
  (
    SELECT emp_dept
      FROM emp_details
      GROUP BY emp_dept
      HAVING COUNT(*) >2
  );



/*
From the following tables write a SQL 
query to find the departments with the second lowest sanction amount. Return emp_fname and emp_lname.
*/

SELECT emp_fname, emp_lname 
FROM emp_details 
WHERE emp_dept IN (
  SELECT dpt_code
  FROM emp_department 
  WHERE dpt_allotment= (
    SELECT MIN(dpt_allotment)
    FROM emp_department 
    WHERE dpt_allotment >
 (SELECT MIN(dpt_allotment) 
      FROM emp_department )));



select nth highest salary from employee
select * from employee group by salary order by salary DESC limit 1,1
select * from employee where salary = (select distinct salary from employee order by salary DESC Limit 1, 1)
