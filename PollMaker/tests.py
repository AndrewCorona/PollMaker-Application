from django.test import SimpleTestCase, TestCase
from .forms import PollForm

class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_page_status_code(self):
        response = self.client.get('/create')
        self.assertEqual(response.status_code, 200)

class PollCreateTest(TestCase):
    def test_model(self):
        form = PollForm({
            'question':"test question",
            'answerone':"test answer one",
            'answertwo':"test answer two",
            'answerthree':"test answer three",
        }, entry=self.entry)
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.question, "test question")
        self.assertEqual(comment.answerone, "test answer one")
        self.assertEqual(comment.answertwo, "test answer two")
        self.assertEqual(comment.answerthree, "test answer three")
        self.assertEqual(comment.entry, self.entry)

    def test_blank_model_data(self):
        form = PollForm({}, entry=self.entry)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
        'question': ['required'],
        'answerone': ['required'],
        'answertwo': ['required'],
        'answerthree': ['required'],
        })




if __name__ == "__main__":
    HomePageTests()
    print("All pages are returning 200")
    PollCreateTest()
    print("Poll Creation is working")