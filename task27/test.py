from helpers import io

io.logger(error_type = "Some mysterious error!",
           code = 888,
           file = __file__,
           line = 31,
           message_ = "I have done a new record!")

from helpers import crypt

crypt.cezary()