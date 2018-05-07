import React from 'react';

class MeetForm extends React.Component{
    render() {
        return (
          <div className='b-create-form'>
              <h2>Новое мероприятие</h2>
              <form>
                  <div className='b-form-field-wrapper'>
                      <input className='b-form-field' type='text' name='title' placeholder='Заголовок'/>
                  </div>
                  <div>
                      <input type='text' name='description'/>
                  </div>
                  <div>
                      <input type='coordinates' name='coordinates'/>
                  </div>
                  <div>
                      <button>Создать</button>
                  </div>
              </form>
          </div>
        );
    }
}

export default MeetForm;