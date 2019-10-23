import config
import vk_api
import random

from logic.task_manager import TaskManager, Task
from logic.love_words import get_rand_word


vk_session = vk_api.VkApi(
    token=config.access_token
)

vk = vk_session.get_api()

tm = TaskManager()
target_user = config.target_user

def send_msg(msg_text):
    vk.messages.send(
        user_id=target_user,
        random_id=random.randint(0, 1000000), 
        message=msg_text
    )


class VKTask(Task):
    def __init__(self, tmp_message, hours: int, minutes: int):
        super().__init__(hours, minutes)
        self.tmp_message = tmp_message

    def run(self):
        named = get_rand_word()
        msg = self.tmp_message.format(
            named
        )
        print('send masg:', msg)

tm.append_task(VKTask('Доброе утро моя {}. Надеюсь ты уже открыла глазки и готова встретить замечательный новый день! Люблю тебя =*', 10, 00))
tm.append_task(VKTask('Добрый день моя {}. Надеюсь ты полна сил чтобы радоваться этому дню дальше! Люблю тебя =*', 14, 00))
tm.append_task(VKTask('Добрый вечер моя {}. Надеюсь ты замечательно провила этот день и готова сматреть сладкий сон с розовыми пони! Люблю тебя =*', 21, 00))
tm.run()