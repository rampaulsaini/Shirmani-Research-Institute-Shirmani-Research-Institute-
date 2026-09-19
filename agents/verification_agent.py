"""Conservative verification labels."""
def classify(text,source=None): return {'status':'source-backed' if source else 'unverified','reason':'Source trace exists; external truth is not implied.'}
def verify(text,evidence=''): return {'text':text,'status':'verified' if evidence else 'unverified','evidence':evidence}
