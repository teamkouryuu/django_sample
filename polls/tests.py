import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question
# Create your tests here.

class QuestionModelsTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        [テスト] test_was_published_recently()未来の日付を設定した場合falseを返す
        """
        time = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


    def test_was_published_recently_with_old1_question(self):
        """
        [テスト] test_was_published_recently()23時間59分59秒前までは最近と判定しtrueを返す
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)


    def test_was_published_recently_with_old2_question(self):
        """
        [テスト] test_was_published_recently()現在から一日前はfalseを返す
        """
        time = timezone.now() - datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
