-- 코드를 입력하세요


select round(avg(
case
when car_type='suv' then daily_fee
end)) as average_fee
from car_rental_company_car