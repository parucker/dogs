import React from 'react';
import UserHeaderNav from './UserHeaderNav';
import styles from './UserHeader.module.css';
import { useLocation } from 'react-router';

const UserHeader = () => {
    const [title, setTitle] = React.useState('');
    const location = useLocation();

    React.useEffect(()=>{      
        var titleAux = location.pathname;
        titleAux = titleAux.split('/');
        titleAux = titleAux[titleAux.length-1];
        titleAux = titleAux.charAt(0).toUpperCase() + titleAux.slice(1);
        if(titleAux==="Conta"){
            titleAux = "Minha Conta";
        }
        setTitle(titleAux);
    }, [location]);

    return (
        <header className={styles.header}>
            <h1 className='title'>{title}</h1>
            <UserHeaderNav />
        </header>
    )
}

export default UserHeader;
