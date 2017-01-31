""" Func test for doing stuff with user data """
import vcr
EXPECTED_MESSAGE = 'w00t!'


class TestFuncCreateUser(object): 
    @vcr.use_cassette
    def test_func_create_user_stores_user_info(self):
        from app import Request, create_user

        test_user = Request(
            username='estherbester', 
            profile='kittens'
        )
        
        result = create_user(test_user)

        assert result == EXPECTED_MESSAGE











#@vcr.use_cassette('my_own_cassette.json', serializer='json', record_mode='all')
#my_vcr = vcr.VCR(serializer='json', record_mode='none', path_transformer=VCR.ensure_suffix('.json')
#@my_vcr.use_cassette
#with vcr.use_cassette():
