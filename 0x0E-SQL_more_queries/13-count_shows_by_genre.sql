-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked
SELECT tg.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS tg
       INNER JOIN `tv_show_genres` AS t
       ON tg.`id` = t.`genre_id`
 GROUP BY tg.`name`
 ORDER BY `number_of_shows` DESC;
