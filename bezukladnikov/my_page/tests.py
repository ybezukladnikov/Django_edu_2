from django.test import TestCase

class TestMyPage(TestCase):

    RIGHT_RESPONSE = 200

    def test_index(self):
        '''
        Тестируем главную страницу приложения.
        client в данном случае это иммитация работы браузера.
        Вызываем метод get для начальной страницы приложения.
        И потом сопоставляем ответ, который получим от сервера
        в нужным нам вариантом
        '''
        response = self.client.get('')
        self.assertEqual(response.status_code, self.RIGHT_RESPONSE)


    def test_raleigh(self):
        response = self.client.get('/category/raleigh')
        self.assertEqual(response.status_code, 301)

