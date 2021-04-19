import React from 'react';
import FeedModal from './FeedModal';
import FeedPhotos from './FeedPhotos';
import PropTypes from 'prop-types';

const Feed = ({user}) => {
  const [modalPhoto, setModalPhoto] = React.useState(null);
  const [pages, setPages] = React.useState([1]);
  const [infinite, setInfinite] = React.useState(true);

  //Infinite scroll
  React.useEffect(()=> {
    let wait = false; 

    function infinitScroll(){
      if(infinite){
        const scroll = window.scrollY;
        const height = document.body.offsetHeight - window.innerHeight;
        if(scroll>height*0.75 && !wait){
          console.log("Teste Scroll");
          setPages((pages) => [...pages, pages.length +1]);
          wait = true;
          setTimeout(()=>{
            wait = false;
          }, 500);
        }
      }
    }
    window.addEventListener('wheel', infinitScroll); //"No scroll with side bar", scroll with wheel of the mouse
    window.addEventListener('scroll', infinitScroll);
    return () =>{
      window.removeEventListener('wheel', infinitScroll);
      window.removeEventListener('scroll', infinitScroll);
    };
  },[infinite]);

  return (
    <div>
      {modalPhoto && (
        <FeedModal photo={modalPhoto} setModalPhoto={setModalPhoto} />
      )}
      {pages.map(page => <FeedPhotos setInfinite={setInfinite} key={page} user={user} page={page} setModalPhoto={setModalPhoto} />)}
    </div>
  );
};

//Test prop-types
Feed.defaultProps = {
  user: 0
}

Feed.propType = {
  user: PropTypes.oneOfType(PropTypes.string.isRequired, PropTypes.number.isRequired),
};

export default Feed;