from indra.statements import *
from indra.assemblers.pybel import PybelAssembler

map2k1 = Agent('MAP2K1', db_refs={'HGNC': '6840'})
mapk1 = Agent('MAPK1', db_refs={'HGNC': '6871'})
stmt = Phosphorylation(map2k1, mapk1, 'T', '185')

pba = PybelAssembler([stmt])
belgraph = pba.make_model()

pba.save_model('out.txt', output_format='bel')

with open('out.txt', 'r') as file:
    contents = file.read()

print(contents)