content = settings.IPAY88_MERCHANT_KEY + settings.IPAY88_MERCHANT_CODE \
          + data['PaymentId'] + data['RefNo'] + amount + data['Currency'] \
          + data['Status']

content = (settings.IPAY88_MERCHANT_KEY + settings.IPAY88_MERCHANT_CODE + data['PaymentId'] + data['RefNo']
           + amount + data['Currency'] + data['Status'])
