import React, {useState} from 'react';

function Dropdown({title, items, multiSelect = false}) {
    const [open, setOpen] = useState();
    const [selection, setSelection] = useState([]); 

    function handleOnClick(item) {}

    return (
        <div className="dd-wrapper">
            <div tabIndex={0} className="dd-header" role="button" onKeyPress={() => toggle(!open)
            }
        </div>
    )
}