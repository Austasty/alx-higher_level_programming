-- script that lists all shows, and all genres linked to that show
SELECT t.`title`, tg.`name`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS ts
       ON t.`id` = ts.`show_id`

       LEFT JOIN `tv_genres` AS tg
       ON ts.`genre_id` = tg.`id`
 ORDER BY t.`title`, tg.`name`;
