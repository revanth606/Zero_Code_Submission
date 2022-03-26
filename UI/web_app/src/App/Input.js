import React from 'react';

/**
 * functional component for handling input fields in auth page
 * @param {*} param0 
 * @returns 
 */
const Input = ({ name, handleChange, label, autoFocus, type }) => (
    <>
        <label>{label}</label>
        <input
        name={name}
        onChange={handleChange}
        required
        // fullWidth
        // autoFocus={autoFocus}
        type={type}
        />
    </>
);

export default Input;