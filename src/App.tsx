import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/pages/home/home';
import Header from './components/sections/header/header';
import footer from './components/sections/footer/footer';

class App extends Component {
  render() {
    return (
      <Router>
          <Routes>
            <Route exact path="/" element={<Home/>}/>
          </Routes>
      </Router>
    );
  }
}

export default App;