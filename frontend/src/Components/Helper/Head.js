import React from 'react';


//Used to change the header according to a specific page

const Head = (props) => {
  React.useEffect(() => {
    document.title = props.title + ' | Dogs';
    document
      .querySelector("meta[name='description']")
      .setAttribute('content', props.description || '');
  }, [props]);

  return <></>;
};

export default Head;