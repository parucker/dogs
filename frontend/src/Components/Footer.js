import React from 'react';
import styles from './Footer.module.css'
import {ReactComponent as Dogs} from '../Assets/dogs-footer.svg'

const Footer = () => {
    return(
        <div className={styles.footer}> 
            <p>Dogs. Alguns Direitos Reservados</p>
        </div>
    )
}

export default Footer;