import apache_beam


# zmienna1 = [1, 3, 5, 7]
# zmienna2 = zmienna1 | apache_beam.Map(lambda x: x * 2)
# print(zmienna2)

class ToKeyV(apache_beam.DoFn):
    def process(self, element, *args, **kwargs):
        x = element.split(',')
        if x[0] == '2': return
        kv = (x[1], x[0])
        return [kv]


with apache_beam.Pipeline() as p:
    linie = p | (apache_beam.io.ReadFromText('trade.csv')
              | apache_beam.ParDo(ToKeyV())
              | apache_beam.GroupByKey()
              | apache_beam.Map(print))
