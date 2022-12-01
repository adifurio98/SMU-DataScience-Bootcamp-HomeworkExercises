-- 1) List the following details of each employee: employee number, last name, first name, sex, and salary.
select
	e.emp_no,
	e.last_name,
	e.first_name,
	e.sex,
	s.salary
from
	employees e
	join salaries s on e.emp_no = s.emp_no
order by
	e.last_name asc
	
-- 2) List first name, last name, and hire date for employees who were hired in 1986.
Select
	e.last_name,
	e.first_name,
	e.hire_date
from
	employees e
where
	extract(year from e.hire_Date) = 1986
order by
e.last_name asc

-- 3) List the manager of each department with the following information
select
	d.dept_no,
	d.dept_name,
	e.last_name,
	e.first_name,
	t.title
from 
	departments d
	join dept_manager dm on d.dept_no = dm.dept_no
	join employees e on dm.emp_no = e.emp_no
	join titles t on e.emp_title_id = t.title_id
order by
	d.dept_no,
	e.last_name
	
-- 4) List the department of each employee with the following information: employee number, last name, first name, and department name.

select
	e.last_name,
	e.first_name, 
	e.emp_no,
	d.dept_no,
	d.dept_name
from
	employees e
	join dept_emp de on e.emp_no = de.emp_no
	join departments d on de.dept_no = d.dept_no
order by
	e.last_name asc
	
-- 5) List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
select
	e.last_name,
	e.first_name,
	e.sex
from
	employees e 
where
	e.last_name like 'B%'and
	e.first_name = 'Hercules'
order by
	e.last_name desc
	
-- 6) List all employees in the Sales department, including their employee number, last name, first name, and department name.
select
	e.last_name,
	e.first_name,
	e.emp_no,
	d.dept_name
from
	employees e
	join dept_emp de on e.emp_no = de.emp_no
	join departments d on de.dept_no = d.dept_no
where 
	d.dept_name = 'Sales'
order by
	e.last_name desc

-- 7) List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select
	e.last_name,
	e.first_name,
	e.emp_no,
	d.dept_name
from
	employees e
	join dept_emp de on e.emp_no = de.emp_no
	join departments d on de.dept_no = d.dept_no
where 
	d.dept_name = 'Sales'or
	d.dept_name = 'Development'
order by
	e.last_name desc

-- 8) List the frequency count of employee last names (i.e., how many employees share each last name) in descending order.
select
	e.last_name,
	count(*) as num_emps
from
	employees e
group by
	e.last_name
order by
	num_emps desc
