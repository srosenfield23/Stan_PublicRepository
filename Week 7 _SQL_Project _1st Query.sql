--compares UK and US employee salaries by dept name
select d.department_id,d.department_name,e.first_name,e.last_name,e.salary,h.location_id, h.city, h.state_province, h.country_id
from hr.departments d
    join hr.locations h
        on d.location_id=h.location_id
    join hr.employees e
        on d.department_id=e.department_id
where country_id='US' or country_id='UK'
order by department_name
