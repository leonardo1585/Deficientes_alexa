from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name, get_slot_value
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response, Intent
from ask_sdk_model.ui import SimpleCard
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_model.dialog import ElicitSlotDirective
import pymysql.cursors


sb = SkillBuilder()


connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='deficientes_projeto'
)

cursor = connection.cursor()


class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = 'Skill em desenvolvimento'

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response


class OpcaoUmIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name('OpcaoUmIntent')(handler_input)


    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        nome = slots["Rua"].value

        speak_output = f'O nome da "{nome}" foi adicionado com sucesso.'

        handler_input.response_builder.speak(speak_output).set_card(
            SimpleCard("Hello World", speak_output)).set_should_end_session(
            True)

        comando_SQL = "INSERT INTO lugar (rua) VALUES (%s)"
        cursor.execute(comando_SQL, (nome))
        connection.commit()

        return handler_input.response_builder.response





class OpcaoDoisIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("OpcaoDoisIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        comando_SQL = 'SELECT * FROM lugar'
        cursor.execute(comando_SQL)
        valores_lidos = cursor.fetchall()
        lista = []
        for c in valores_lidos:
            lista.append(c)

        values = ' '.join(str(v) for v in lista)

        handler_input.response_builder.speak(values).set_card(
            SimpleCard("Hello World", values)).set_should_end_session(
            True)
        return handler_input.response_builder.response


class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(
            handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Goodbye!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(True)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # any cleanup logic goes here

        return handler_input.response_builder.response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(OpcaoUmIntentHandler())
sb.add_request_handler(OpcaoDoisIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())