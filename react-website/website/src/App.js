import React, { useState } from 'react'
import { data } from './json_formatted.js'
import { Container, Table, Credits } from './styles'
import './App.css';
import { FaLink, FaExternalLinkAlt } from 'react-icons/fa'
import Image1 from './assets/logo.png'
import Image2 from './assets/dione.png'

function App() {

  // FILTRA POR MATÉRIAS E COLOCA EM ORDEM ALFABÉTICA
  const filteredData = data.filter((v, i, a) =>
    a.findIndex(v2 =>
      (v.subject === v2.subject)) === i)
    .sort(function (a, b) {
      let objA = a.subject.toUpperCase().normalize("NFD").replace(/\p{Diacritic}/gu, "");
      let objB = b.subject.toUpperCase().normalize("NFD").replace(/\p{Diacritic}/gu, "");
      return (objA < objB) ? -1 : (objA > objB) ? 1 : 0;
    });

  return (
    <Container>
        <Table>
          <thead>
            <tr>
              <th>Matéria</th>
              <th>Professor</th>
              <th>Link</th>
            </tr>
          </thead>
          <tbody>
            {filteredData.map((item) =>
            (<tr className="post-item">
              <td>{item.subject}</td>
              <td>{item.teacher}</td>
              <td className="link-button">
                <a href={item.subject_url} target="_blank" >
                  <FaLink />
                </a>
              </td>
            </tr>)
            )}
          </tbody>
        </Table>
        <Credits>
          <p>Atualmente essa página possui {filteredData.length} matérias.</p>
          <p>Feito por Lucas Nascimento</p>
          <a href="https://www.github.com/lucasnsaraujo" target="_blank"> Github </a>
        </Credits>
    </Container>
  );
}

export default App;
