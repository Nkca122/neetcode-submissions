-- Write your query below
alter table employees add
bonus int;

update employees
set bonus = case
when employee_id % 2 > 0 and name not like 'M%' then salary
else 0
end;

select employee_id, bonus from employees order by employee_id asc;