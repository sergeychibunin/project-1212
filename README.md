# project-1212

# Examples

```bash
$ curl http://0.0.0.0:8000/api/page/
{"count":11,"next":"http://0.0.0.0:8000/api/page/?limit=10&offset=10","previous":null,"results":[{"id":1,"url":"http://0.0.0.0:8000/api/page/1/"},{"id":2,"url":"http://0.0.0.0:8000/api/page/2/"},{"id":3,"url":"http://0.0.0.0:8000/api/page/3/"},{"id":4,"url":"http://0.0.0.0:8000/api/page/4/"},{"id":5,"url":"http://0.0.0.0:8000/api/page/5/"},{"id":6,"url":"http://0.0.0.0:8000/api/page/6/"},{"id":7,"url":"http://0.0.0.0:8000/api/page/7/"},{"id":8,"url":"http://0.0.0.0:8000/api/page/8/"},{"id":9,"url":"http://0.0.0.0:8000/api/page/9/"},{"id":10,"url":"http://0.0.0.0:8000/api/page/10/"}]}

$ curl http://0.0.0.0:8000/api/page/1/
{"id":1,"title":"Demo page 1","texts":[{"title":"Demo Text 1","body":"There is big content 1"}],"audios":[{"title":"Demo Audio 1","audio_url":"http://u.rl/1.mp3","rate":320}],"videos":[{"title":"Demo Video 1","video_url":"http://u.rl/1.mp4","subtitles_url":"http:/u.rl/1-subt.srt"}]}
```
