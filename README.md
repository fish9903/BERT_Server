# 감정 분석을 위한 서버

학습된 모델 다운받고 파일을 `DjangoServer\AI_models\models` 에 저장해야 함 (용량문제)
- [모델 링크](https://drive.google.com/file/d/1r3Mh6zUfkB9RLrJHYGrgX909p5dC5dfu/view?usp=drive_link)

## 필요 패키지 설치(python 3.9.17)
```
pip install numpy==1.23.5
pip install mxnet -f https://dist.mxnet.io/python/cpu
pip install gluonnlp==0.8.0 pandas tqdm
pip install sentencepiece
pip install transformers
pip install torch
pip install sentence-transformers
```

## 설정 후 시작
`python manage.py runserver` --> `http://127.0.0.1:8000/post/` 접속
