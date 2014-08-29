from bottle import route
from mailchute import db
from mailchute.model import IncomingEmail, RawMessage
from mailchute.api.serializer import (
    response, ResponseDTO, IncomingEmailDTO, RawMessageDTO)


@route('/inbox/<recipient>/')
@response('incoming_emails', IncomingEmailDTO)
def get_incoming_emails(recipient):
    return (
        db.session.query(IncomingEmail).filter_by(recipient=recipient).all()
    )


@route('/inbox/<recipient>/raw_message/<raw_message_id>')
@response('raw_messages', RawMessageDTO)
def get_raw_message(recipient, raw_message_id):
    return (
        db.session.query(RawMessage).join(IncomingEmail)
        .filter(IncomingEmail.recipient == recipient)
        .filter(RawMessage.raw_message_id == raw_message_id)
        .one()
    )
