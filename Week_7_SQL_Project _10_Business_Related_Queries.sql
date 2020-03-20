--1. compares UK and US employee salaries by Department showing higher salary by each dept on top.
-- in the query below, the first join operator uses the location_id column to link both departments and locations tables together
-- and the second join operator uses the department_id column to link the employees and departments tables to add additional columns: employee names and salary

select e.first_name,e.last_name,e.salary,d.department_id,d.department_name,h.location_id, h.city, h.state_province, h.country_id
  from hr.departments d
    join hr.locations h
        on d.location_id=h.location_id
    join hr.employees e
        on d.department_id=e.department_id
where country_id='US' or country_id='UK'
order by department_name,salary desc;


-- 2. how many unique/distinct company locations are located outside of United States? Answer is: 13
-- in this subquery below, utilizes the count () function to count the number of unique countries,
-- and the where clause excludes the US.

select count(country_id) as Number_Of_Distinct_Company_Locations_Outside_US
  from (
    select country_id, count(country_id) as Unique_Countries
      from hr.locations
where country_id != 'US'
Group by country_id
);


--3. How many employees were hired between 2002 and 2005 inclusive
-- this query, utilizes the count () function and between operator to obtain the number of employees hired between years: 2002-2005.
select count(hire_date) as Number_Hired_Between_2002_and_2005_inclusive
  from hr.employees
where to_char(hire_date,'YY') between '02' and '05';


--4. find the lowest salary by Job Title, exluding President and VP.
-- this query, utilizes the min() function to determine the lowest salary.
select job_id,min(salary) as Lowest_Salary_by_JOB
  from hr.employees
where job_id != 'AD_PRES' and JOB_ID != 'AD_VP'
Group by job_id
order by MIN(Salary) desc;


--5. Who is the highest-paid employee with a name that starts with the letter 'J', and what is their Salary
-- this query, utilizes the max () function to determine the highest salary, and the percent wild card symbol to filter out the first names.
select first_name, last_name, salary as Max_Sal__First_Name_Start_J
  from hr.employees
where salary =
(
select MAX(salary)
  from hr.employees
where first_name like 'J%'
);


--6. Display products by pages, showing the list price from high to low. If each page has 10 products, display only the fourth page.
-- in this query below, the CTE uses the ROW_NUMBER() function to assign each row a sequential integer in descending order.
-- The outer query retrieves the row whose row numbers are between 41 and 50.

with cte_products AS (
    select
        row_number() over(
            order by list_price desc
        ) row_num,
        product_name,
        list_price
    from
        OE.product_information
)
    select * from cte_products
WHERE row_num > 40 and row_num <= 50;


-- 7. What are each Customer's Order Totals, showing by (last_name, first_name), and sorted from highest to lowest
-- in this query below, the CTE uses the SUM () function to find the order_total for each customer_id
with o as (
    select customer_id, sum(order_total) as order_total
    from
        oe.orders
    group by customer_id
    order by order_total desc
)

select c.customer_id, cust_last_name || ', ' || cust_first_name as full_name, to_char(o.order_total, 'l99G9999') as Customers_Order_Totals
    from
        oe.customers c
          left join o on c.customer_id = o.customer_id
          where order_total is not null
          order by order_total desc


--8. How many employees are in Sales
-- in this query below, the count() function sums up the total number of Sales Employees
select count(job_id) as Number_Sales_Employees
  from
    hr.employees
where department_id = 80;

--9. How many US and UK employees are there combined? Answer=103
-- in this subquery below, it executes first, extracting the employees and locations,
-- then the outer query, counts the number of countries to give us the final results

select count(country_id) as Total_Of_US_and_UK_Employees
  from (
    select e.first_name,e.last_name,h.location_id, h.city, h.state_province, h.country_id
      from hr.departments d
        join hr.locations h
          on d.location_id=h.location_id
        join hr.employees e
          on d.department_id=e.department_id
where country_id='US' or country_id='UK'
)


--10. What year and month generates the most sales? Answer is: 1998-04
-- in this subquery below, the sum () function sums up the total sales by year and month,
-- and the external query, filter rownum, extracts out the year and month with the highest sales.
select most_sales_by_yr_month
  from
(
  select
    prod_id,
    to_char(TIME_ID, 'YYYY-MM') as most_sales_by_yr_month,
    sum(amount_sold) as total_sold
        from
            SH.SALES
group by to_char(TIME_ID, 'YYYY-MM'), prod_id
order by total_sold desc
)
where rownum=1
