from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .apps import ServerConfig
from django.views.decorators.csrf import csrf_exempt
import json

# test
def testapp_index(request):
    return HttpResponse("장고 테스트앱 입니다.")

def KcBERT_result(request):
    result = ServerConfig.KcBERT.predict("하.... 이 놈의 나라 노인네들은 또 의병이 나라 지키기를 원하는 건가??? 정녕 니 후손들이 통일된 민족, 좋은 나라, 공정한 나라에서 사는 게 그렇게 싫더냐? 미친 노인네들 어휴...")
    return HttpResponse("emotion: {}".format(result))

@csrf_exempt
def post_view(request):
    return HttpResponse('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script>

    function send() {
        alert("send");
        document.getElementById("contents").submit();
    }
    </script>
</head>
<body>
    <form id="contents" name="contents" method="post" action="http://127.0.0.1:8000/parameter">
        text : 윤석열 대통령이 우리나라를 답방하는 기시다 후미오 일본 총리와 7일 정상회담을 갖고 북핵대응은 물론 경제안보 협력, 미래세대 교류 확대, 후쿠시마 원전 오염수 방류 문제 등 양국 현안을 폭넓게 논의할 예정이다.
            3월 일본에서처럼 양국 정상 부부가 함께 하는 만찬 등 친교의 시간도 이어진다.
            이도운 대통령실 대변인은 4일 오후 용산 대통령실 청사에서 브리핑을 열고 \"윤 대통령은 7일 대통령실에서 기시다 총리와 회담을 갖고 안보와 첨단산업 및 과학기술, 청년 및 문화협력 등 양국간 주요 관심사에 대해 협의할 예정\"이라며 \"이번 방한은 양국간 셔틀외교가 본격 가동되는 의미가 있다\"고 밝혔다.
            이 대변인에 따르면 윤 대통령과 기시다 총리는 7일 소인수회담과 확대회담을 연이어 열고 공동기자회견에 나선다. 다만 이번 답방이 윤 대통령의 3월 방일 때와 같이 '실무방문'이기 때문에 공동선언이나 공동성명 등이 발표되지는 않을 것으로 보인다.
            '국빈방문'이나 '공식방문'보다 의전 등 관련 절차가 간소한 '실무방문'에서는 공동선언 등이 나오는 경우가 흔치 않다.
            대통령실 핵심관계자는 \"공동 기자회견은 하겠지만 어떤 선언이 나온다, 그거는 어려운 것 같다\"고 했다.
            정상회담에서는 후쿠시마 원전 오염수 방류 문제도 다뤄질 전망이다.
            대통령실 핵심관계자는 \"국민 여러분이 중요한 문제라고 생각한다면 굳이 우리가 현안에서 제외할 필요는 없다고 생각한다\"고 밝혔다.
            다만 후쿠시마산 수산물 수입은 앞으로도 계속 금지된다.
            대통령실은 원전 오염수 방류가 과학적으로 문제가 없는지 따지는 것과 수산물 수입은 별개라는 입장이다.
            청년 등 미래세대 지원을 위해 한일 양국이 공동기금을 설치하는 방안 등도 논의된다. 이 관계자는 "한일을 포함한 모든 나라 정상간 협의에서는 청년을 포함한 미래세대를 위해 무엇을 할지가 관심사이기 때문에 그에 따라 (공동기금 등을) 협의를 할 것"이라고 밝혔다.
            공동기자회견 이후에는 윤 대통령과 김건희 여사, 기시다 총리와 기시다 유코 여사가 함께 하는 만찬 등 친교의 시간이 이어진다.
            윤 대통령 부부가 관저로 기시다 내외를 초청하는 방안이 유력하다. 만찬에는 한우불고기와 청주 등이 오를 것으로 보인다.
            이 관계자는 " 외국 정상이 오면 우리가 한식으로 대접할 가능성이 많겠다. (한우불고기 관련 보도도) 그런 차원에서 이해한다"며 술 종류에 대해서는 "기시다 총리가 손님이니까 선호하는 술이 있다면 그것을 준비하는 게 옳지 않겠느냐. 기시다 총리가 사케를 좋아한다는 보도가 있어서 비슷한 술인 청주(얘기)가 나온 게 아닌가 한다"고 말했다.
            만찬주로는 여러 종류의 술이 준비될 가능성이 높다.
            앞서 기시다 총리는 전날 윤 대통령을 예방한 아키바 다케오 일본 국가안전보장국장을 통해 '한일관계 개선을 주도한 대통령님의 용기있는 결단을 높이 평가하며, 이에 조금이나마 보답하는 마음으로 이번 답방을 결심하게 되었다'는 메시지를 전달했다.
        
        <br><br>                
        comment : <input name="comment" type="text">
        <button type="button" onclick="send();">전송</button>
    </form>
</body>
</html>''')

@csrf_exempt
def post_test(request):
    if request.method == 'POST':
        comment_arr = []
        comment = request.POST['comment']
        # text = request.POST['text']
        emotion = ServerConfig.KcBERT.predict(comment)


        corpus = ["윤석열 대통령이 우리나라를 답방하는 기시다 후미오 일본 총리와 7일 정상회담을 갖고 북핵대응은 물론 경제안보 협력, 미래세대 교류 확대, 후쿠시마 원전 오염수 방류 문제 등 양국 현안을 폭넓게 논의할 예정이다",
            "3월 일본에서처럼 양국 정상 부부가 함께 하는 만찬 등 친교의 시간도 이어진다.",
            "이도운 대통령실 대변인은 4일 오후 용산 대통령실 청사에서 브리핑을 열고 \"윤 대통령은 7일 대통령실에서 기시다 총리와 회담을 갖고 안보와 첨단산업 및 과학기술, 청년 및 문화협력 등 양국간 주요 관심사에 대해 협의할 예정\"이라며 \"이번 방한은 양국간 셔틀외교가 본격 가동되는 의미가 있다\"고 밝혔다.",
            "이 대변인에 따르면 윤 대통령과 기시다 총리는 7일 소인수회담과 확대회담을 연이어 열고 공동기자회견에 나선다. 다만 이번 답방이 윤 대통령의 3월 방일 때와 같이 '실무방문'이기 때문에 공동선언이나 공동성명 등이 발표되지는 않을 것으로 보인다.",
            "'국빈방문'이나 '공식방문'보다 의전 등 관련 절차가 간소한 '실무방문'에서는 공동선언 등이 나오는 경우가 흔치 않다.",
            "대통령실 핵심관계자는 \"공동 기자회견은 하겠지만 어떤 선언이 나온다, 그거는 어려운 것 같다\"고 했다.",
            "정상회담에서는 후쿠시마 원전 오염수 방류 문제도 다뤄질 전망이다.",
            "대통령실 핵심관계자는 \"국민 여러분이 중요한 문제라고 생각한다면 굳이 우리가 현안에서 제외할 필요는 없다고 생각한다\"고 밝혔다. ",
            "다만 후쿠시마산 수산물 수입은 앞으로도 계속 금지된다.",
            "대통령실은 원전 오염수 방류가 과학적으로 문제가 없는지 따지는 것과 수산물 수입은 별개라는 입장이다.",
            '청년 등 미래세대 지원을 위해 한일 양국이 공동기금을 설치하는 방안 등도 논의된다. 이 관계자는 "한일을 포함한 모든 나라 정상간 협의에서는 청년을 포함한 미래세대를 위해 무엇을 할지가 관심사이기 때문에 그에 따라 (공동기금 등을) 협의를 할 것"이라고 밝혔다.',
            "공동기자회견 이후에는 윤 대통령과 김건희 여사, 기시다 총리와 기시다 유코 여사가 함께 하는 만찬 등 친교의 시간이 이어진다.",
            "윤 대통령 부부가 관저로 기시다 내외를 초청하는 방안이 유력하다. 만찬에는 한우불고기와 청주 등이 오를 것으로 보인다. ",
            '이 관계자는 " 외국 정상이 오면 우리가 한식으로 대접할 가능성이 많겠다. (한우불고기 관련 보도도) 그런 차원에서 이해한다"며 술 종류에 대해서는 "기시다 총리가 손님이니까 선호하는 술이 있다면 그것을 준비하는 게 옳지 않겠느냐. 기시다 총리가 사케를 좋아한다는 보도가 있어서 비슷한 술인 청주(얘기)가 나온 게 아닌가 한다"고 말했다.',
            "만찬주로는 여러 종류의 술이 준비될 가능성이 높다.",
            "앞서 기시다 총리는 전날 윤 대통령을 예방한 아키바 다케오 일본 국가안전보장국장을 통해 '한일관계 개선을 주도한 대통령님의 용기있는 결단을 높이 평가하며, 이에 조금이나마 보답하는 마음으로 이번 답방을 결심하게 되었다'는 메시지를 전달했다."
            ]
        comment_arr.append(comment)
        related = ServerConfig.SBERT.analysis(corpus, comment_arr)
        print("***********")
        print(related)
        related_text = related['text']
        related_score = related['score']
        data = {
            #'text': text,
            'text': corpus,
            'comment': comment,
            'emotion': emotion,
            'related_text': related_text,
            'related_score': related_score,
        }

        # HTML 템플릿 문자열에 데이터 삽입
        html_response = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <p>분석 결과</p>
    <br><br>
    <strong>본문</strong>: {data['text']}
    <br><br>
    <strong>댓글</strong>: {data['comment']}
    <br><br>
    <strong>감정</strong>: {data['emotion']}
    <br><br>
    <strong>원인</strong>: {data['related_text']}
    <br><br>
    <strong>점수</strong>: {data['related_score']}
</body>
</html>'''

        return HttpResponse(html_response)