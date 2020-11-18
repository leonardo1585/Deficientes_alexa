from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name, get_slot_value
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response, Intent
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model.dialog import ElicitSlotDirective
import json
import requests
from airtable import Airtable


key = 'keyda2y1mcH9pIIOS'
airtable = Airtable('appXVFxRam3NYPQlM/', 'Table 1', key)
airtable.get_all()
sb = SkillBuilder()
lugar = []

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
        speak_output = 'Qual o nome do lugar e o nome do estado?'

        handler_input.response_builder.speak(speak_output).ask(speak_output).set_card(
            SimpleCard("Hello World", speak_output)).set_should_end_session(
            False)

        return handler_input.response_builder.response



class OpcaoDoisIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("OpcaoDoisIntent")(handler_input)

    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        nome = slots["Rua"].value
        cidade = slots["Estado"].value

        speak_output = f'O local "{nome}" no estado de "{cidade}" foi adicionado com sucesso.'

        airtable.insert({'Lugar': f'{nome}', 'Estado': f'{cidade}'})

        handler_input.response_builder.speak(speak_output).set_card(
            SimpleCard("Hello World", speak_output)).set_should_end_session(
            True)

        return handler_input.response_builder.response


class PegarCidadeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name('PegarCidadeIntent')(handler_input)


    def handle(self, handler_input):
        ask_output = 'Qual o nome do seu estado?'

        handler_input.response_builder.speak(ask_output).ask(ask_output).set_card(
            SimpleCard("Hello World", ask_output)).set_should_end_session(
            False)

        return handler_input.response_builder.response


class LerDadosIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name('LerDadosIntent')(handler_input)


    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots
        estado = slots['estadinho'].value
        filtro = airtable.search('Estado', f'{estado}')
        lista = []
        for n, c in enumerate(filtro):
            lista.append(filtro[n]['fields']['Lugar'])

        values = ', '.join(str(v) for v in lista)

        handler_input.response_builder.speak(values).set_card(
            SimpleCard("Hello World", values)).set_should_end_session(
            False)
        return handler_input.response_builder.response




class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(
            handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Cancelando!"

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
sb.add_request_handler(PegarCidadeIntentHandler())
sb.add_request_handler(LerDadosIntentHandler())
<<<<<<< HEAD
sb.add_request_handler(SessionEndedRequestHandler())
=======
sb.add_request_handler(SessionEndedRequestHandler())
>>>>>>> d74fbbecdcaaa8667e69ae2b2df699d70d6dd058
