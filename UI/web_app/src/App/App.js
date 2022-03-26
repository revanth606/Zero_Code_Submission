import React, {useState} from 'react';
import './App.css';
import Input from './Input';

/**
 * functional component for handling landing page
 * @param {*} param0 
 * @returns 
 */
function App() {
  const [form, setForm] = useState({name:'',zip:''});
  const [output, setOutput] = useState('');

  /**
     * method to monitor changes in form values and store them in form variable
     * @param {*} event 
     */

  const handleChange = function(event) {
    setForm({ ...form, [event.target.name]: event.target.value });
  }

  /**
     * method to handle submit button click which calls the backend api with form values, receives and displays the output
     * @param {*} event 
     */
   const handleSubmit = async function(event) {
    try {
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)};
        fetch('http://127.0.0.1:5000/create_phrase', requestOptions)
        .then(response => response.json())
        .then((data) => setOutput(data.response));
      
    } catch (error) {
        console.log(error.response.data.message)
        setOutput(error.response.data.message)
    }
    
    event.preventDefault();
  }

  return (
    <>
    <form className="signupform">
      <Input name="name" label="Name" handleChange={handleChange}></Input>
      <Input name="zip" label="Zip Code" handleChange={handleChange}></Input>
      <button className="register" type="submit" onClick={handleSubmit}>Submit</button>
    </form>
    <p>{output}</p>
    </>
  );
}

export default App;
