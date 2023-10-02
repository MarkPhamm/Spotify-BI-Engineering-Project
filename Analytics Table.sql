DROP TABLE `analytics`;

CREATE TABLE "spotify_db"."analytics" WITH (format = 'parquet') AS 

WITH dim_album_cte AS (
  SELECT 
    DISTINCT * 
  FROM 
    dim_album_data
), 
dim_artist_cte AS (
  SELECT 
    DISTINCT * 
  FROM 
    dim_artist_data
) 
SELECT 
  fact_songs_data.song_id, 
  fact_songs_data.song_name, 
  fact_songs_data.duration_ms / 1000 AS song_duration_seconds, 
  fact_songs_data.url AS song_url, 
  fact_songs_data.popularity AS song_popularity, 
  SUBSTRING(fact_songs_data.song_added FROM 1 FOR 19) as song_added,
  artist_id, 
  artist_name, 
  dim_album_cte.album_name, 
  dim_album_cte.release_date AS album_release_date, 
  dim_album_cte.total_tracks AS album_total_tracks, 
  dim_album_cte.url AS album_url, 
  fact_songs_data.record_date 
FROM 
  fact_songs_data 
  JOIN dim_album_cte using(album_id) 
  JOIN dim_artist_cte using(artist_id)
