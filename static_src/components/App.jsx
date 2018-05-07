import React from 'react';

import MeetForm from './MeetForm';
import MeetList from './MeetList';

import apiUrls from './../constants/apiUrls';
import './../styles/base.scss';

class App extends React.Component {
    state = {
        meetList: [],
        isLoading: false,
    };

    componentDidMount() {
        this.setState({ isLoading: true });
        fetch(apiUrls.meet, {
            credentials: 'include',
        }).then(
            body => body.json(),
        ).then(
            json => this.setState({ meetList: json.results, isLoading: false }),
        );
        console.log();
    };

    onMeetCreate = (meet) => {
        this.setState({
            meetList: [meet, ...this.state.meetList],
        });
    };

    render() {
        return (
            <div className='b-wrapper'>
                <h1>Список мероприятий</h1>
                <MeetForm onCreate={this.onMeetCreate()}/>
                <MeetList onLoading={this.state.isLoading} meetList={this.state.meetList}/>
            </div>
        );
    }
}

export default App;
