from redis import StrictRedis
from pyotp import random_base32,TOTP
from django.conf import settings
from django.core.mail import send_mail

class OTPService:
    
    redis = StrictRedis(
        host=settings.HOST_REDIS,
        port=settings.PORT_REDIS,
        db=0, 
        decode_responses=True
        )
    
    
    @classmethod
    def generate_otp(cls, email):
        secret = random_base32()
        cls.redis.setex(email, settings.TTL_OTP, secret, )
        hotp = TOTP(secret,interval=settings.TTL_OTP )
        return hotp.now()
    
    @classmethod
    def send_otp_email(cls, email, otp):
        subject = "Ваш OTP код"
        message = f"Ваш OTP код: {otp}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

    
    @classmethod
    def store_otp(cls, email, otp):
        cls.redis.setex(email, settings.TTL_OTP, otp)

    @classmethod
    def get_stored_otp(cls, email):
        return cls.redis.get(email)

    @classmethod
    def delete_otp(cls, email):
        cls.redis.delete(email)

    @classmethod
    def verify_otp(cls, email, otp):
        secret = cls.redis.get(email)
        if not secret:
            return False
        totp = TOTP(secret, interval=settings.TTL_OTP)
        return totp.verify(otp)
    


