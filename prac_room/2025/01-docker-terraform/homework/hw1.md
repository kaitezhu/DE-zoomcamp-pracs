## Question 1. Version of pip

(base) ktzhu@KaitedeMBP 1_docker_sql % docker run -it --entrypoint=bash python:3.12.8

root@bf6070e95d49:/# pip -V
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)

Answer: 24.3.1

## Question 2. Docker networking and docker-compose

The hostname is essentially the service name provided in the yaml file, (in this case db), services can communicate with each other using hostnames.
We use ports from the container (5432) to communicate instead of the mapped port. So db:5432.

Answer: db:5432

## Question 3. Trip Segmentation Count

SELECT 
	case 
		when trip_distance <= 1 then 'Up to 1 mile'
		when trip_distance > 1 and trip_distance <= 3 then '1 - 3 miles'
		when trip_distance > 3 and trip_distance <= 7 then '3 - 7 miles'
		when trip_distance > 7 and trip_distance <= 10 then '7 - 10 miles'
		when trip_distance > 10 then 'Over 10 miles'
	end as trip_segments,
	count(1) as trip_number
FROM public.green_taxi_trips
where 
	cast(lpep_pickup_datetime as date) >= '2019-10-01'
and cast(lpep_dropoff_datetime as date) < '2019-11-01'
group by
	case 
		when trip_distance <= 1 then 'Up to 1 mile'
		when trip_distance > 1 and trip_distance <= 3 then '1 - 3 miles'
		when trip_distance > 3 and trip_distance <= 7 then '3 - 7 miles'
		when trip_distance > 7 and trip_distance <= 10 then '7 - 10 miles'
		when trip_distance > 10 then 'Over 10 miles'
	end;

------------output------------
"1 - 3 miles"	198924
"3 - 7 miles"	109603
"7 - 10 miles"	27678
"Over 10 miles"	35189
"Up to 1 mile"	104802

Answer: 104,802; 198,924; 109,603; 27,678; 35,189

## Question 4. Longest trip for each day

select
	date(lpep_pickup_datetime) as lpep_pickup_datetime,
	max(trip_distance) as max_distance
from public.green_taxi_trips
group by date(lpep_pickup_datetime)
order by max(trip_distance) desc
limit 1;

------------output------------
"2019-10-31"	515.89

Answer: 2019-10-31

## Question 5. Three biggest pickup zones

select 
	date(lpep_pickup_datetime) as lpep_pickup_datetime,
	"PULocationID",
	t2."Zone",
	sum(total_amount) as total_amount_all
from public.green_taxi_trips t1
join public.taxi_zone_lookup t2
on t1."PULocationID" = t2."LocationID"
group by 
	date(lpep_pickup_datetime),
	"PULocationID",
	t2."Zone"
having sum(total_amount) > 13000
and date(lpep_pickup_datetime) = '2019-10-18';

------------output------------
"2019-10-18"	74	"East Harlem North"	18686.680000000084
"2019-10-18"	75	"East Harlem South"	16797.260000000068
"2019-10-18"	166	"Morningside Heights"	13029.790000000039

Answer: East Harlem North, East Harlem South, Morningside Heights

## Question 6. Largest tip

with filtered_trips as (
	select *
	from public.green_taxi_trips
	where EXTRACT(YEAR FROM lpep_pickup_datetime::timestamp) = 2019
	and EXTRACT(MONTH FROM lpep_pickup_datetime::timestamp) = 10
),
EHN_pickup as (
	select ft.*, tz."Zone"
	from filtered_trips ft
	join public.taxi_zone_lookup tz on ft."PULocationID" = tz."LocationID"
	where tz."Zone" = 'East Harlem North'
),
largest_tip as (
	select ep."Zone", max(tip_amount)
	from EHN_pickup ep
	join public.taxi_zone_lookup tz on ep."DOLocationID" = tz."LocationID"
	group by ep."Zone"
	order by max(tip_amount) desc
	limit 1
)
select * from largest_tip;

------------output------------
"East Harlem North"	87.3

Answer: East Harlem North

## Question 7. Terraform Workflow

Downloading the provider plugins and setting up backend
-- terraform init (Downloads required provider plugins and sets up the backend for storing state)
Generating proposed changes and auto-executing the plan
-- terraform apply -auto-approve (-auto-approve flag skips the manual approval step)
Remove all resources managed by terraform
-- terraform destroy

Answer: terraform init, terraform apply -auto-approve, terraform destroy
