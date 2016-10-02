import facebook
my_token = "EAAN7unK1SmkBAKwXN1A9qfxU76AoVuqTURSDEWmfsnmcH3mX0JlRlOku4loy5IHpHZBtCHezaiDyQ5Pm6T2mAZB0jbuDMNdthZAFujg1gxPvMVq8LtgZAm4V7vAfKladj99gA9sS9Np37iIzWJUkhPFgJAt19HVoISqFZBaYRUwZDZD"
my_id = "1664030033909655"
graph = facebook.GraphAPI(access_token=my_token)
slicfin = "%s has just finished slicing a %s!"

graph.put_object(parent_object=my_id, connection_name='feed', message='Hello, world!')