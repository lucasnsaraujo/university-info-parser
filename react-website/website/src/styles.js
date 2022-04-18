import styled from 'styled-components'

export const Table = styled.table`
    border-radius: 10px;
    padding: 20px 10px;
    font-family: 'Poppins';
    max-width: 2000px;
    background: rgba(255, 255, 255, 0.7);

    .link-button {
        display: flex;
        justify-content: center;
        max-width: 60px;
    }

    thead {
        max-width: 60px;
        font-weight: bold;
    }

    td {
        padding: 10px 15px;
        min-height: 110px;
        max-height: 1000px;
        max-width: 600px;
    }

    a {
        background-color: #03045e;
        padding: 5px 20px;
        max-height: 60px;
        margin-top: 15px;

        display: flex;
        justify-content: center;
        align-items: center;

        border-radius: 5px;
        color: #ade8f4;
        text-decoration: none;
    }

    a:hover {
        opacity: 60%;
        transition: 0.5s;
    }

    @media only screen and (max-width: 600px) {
        * {
            font-size: 14px;
            padding: 4px 8px;
        }
        td, a {
            padding: 5px 10px;
           
        }
        margin: 0px 30px;
    }
`

export const Container = styled.div`
    padding: 40px 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: linear-gradient(78deg, #4097cd, #c597cdb8);

    @media only screen and (max-width: 600px) {
        width: fit-content;
        padding: 20px;
    }
`

export const Credits = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

    p {
        font-family: 'Poppins';
        margin-top: 40px;
    }
    
    a {

        background-color: darkblue;
        color: lightblue;
        padding: 4px 10px;
        border-radius: 10px;
        text-decoration: none;
        font-family: 'Poppins';
    }

    a:hover {
        opacity: 0.5;
        transition: 0.2s;
    }
`