-- Write your query below
select u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance 
from users u
left join rides r
on r.user_id = u.id
group by u.name
ORDER BY travelled_distance DESC, u.name ASC;