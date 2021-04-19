import React from 'react';
import Input from '../Forms/Input'
import Button from '../Forms/Button'
import useForm from '../../Hooks/useForm'
import useFetch from '../../Hooks/useFetch'
import { PASSWORD_RESET } from '../../api'
import Error from '../Helper/Error'
import { useNavigate } from 'react-router';

const LoginPasswordReset = () => {
    const [login, setLogin] = React.useState('');
    const [key, setKey] = React.useState('');
    const password = useForm();
    const {error, loading, request} = useFetch();
    const navigate = useNavigate();

    React.useEffect(() => {
        const params = new URLSearchParams(window.location.search);
        const key = params.get('key');
        const login = params.get('login');
        if (key) setKey(key);
        if (login) setLogin(login);
    }, []);

    async function handleSubmit(event){
        event.preventDefault();
            if(password.validate()){
            const {url, options} = PASSWORD_RESET({
                login, key, password: password.value
            })
            const {response} = await request(url, options)
            if(response.ok) navigate('/login');
        }
    }

    return (
        <section className='animeLeft'>
            <h1 className='title'>Mude sua Senha</h1>
            <form onSubmit={handleSubmit}>
                <Input label="Nova senha" type="password" name="password" {...password}/>
                {loading ?   <Button disabled>Mudando...</Button>
                         :   <Button>Trocar Senha</Button>
                }
                <Error error={error} />
            </form>
        </section>
    )
}

export default LoginPasswordReset
