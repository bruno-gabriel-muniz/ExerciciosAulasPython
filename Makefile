format:
	@blue Exercicios/
	@blue tests/
testAll:
	@pytest -v -s
testLessDone:
	@pytest -v -s -m "not Done"