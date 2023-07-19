
import React, { useState } from 'react';
import axios from 'axios';
import { Button, Container, Form, Table } from 'react-bootstrap';

const EventList = () => {
  const [events, setEvents] = useState([]);
  const [username, setUsername] = useState('');
  const [event_type, setEventType] = useState('');
  const [event_source, setEventSource] = useState('');
  const [course_id, setCourseId] = useState('');
  const [fecha, setFecha] = useState('');
  const [hora, setHora] = useState('');
  const handleFilter = () => {

    axios
      .get('http://localhost:8000/userl', {
        params: {
          username: username,
          event_type: event_type,
          event_source: event_source,
          course_id: course_id,
          fecha: fecha,
          hora: hora
        },
      })
      .then((response) => {
        setEvents(response.data.events);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const limitedEvents = events.slice(0, 230);
  return (
    <Container>
      <h1>Lista de Eventos</h1>
      <Form>
        <Form.Group>
          <Form.Label>Username:</Form.Label>
          <Form.Control
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </Form.Group>
        <Form.Group>
          <Form.Label>Event Type:</Form.Label>
          <Form.Control
            type="text"
            value={event_type}
            onChange={(e) => setEventType(e.target.value)}
          />
        </Form.Group>
        <Form.Group>
          <Form.Label>Event Source:</Form.Label>
          <Form.Control
            type="text"
            value={event_source}
            onChange={(e) => setEventSource(e.target.value)}
          />
        </Form.Group>
        <Form.Group>
          <Form.Label>Course ID:</Form.Label>
          <Form.Control
            type="text"
            value={course_id}
            onChange={(e) => setCourseId(e.target.value)}
          />
        </Form.Group>
          <Form.Label>Fecha:</Form.Label>
          <Form.Control
            type="date"
            value={fecha}
            onChange={(e) => setFecha(e.target.value)}
          />
        <Form.Group>
        </Form.Group>
          <Form.Label>Hora:</Form.Label>
          <Form.Control
            type="time"
            value={hora}
            onChange={(e) => setHora(e.target.value)}
          />
        <Form.Group>
        </Form.Group>
        {/* <Button variant="primary" onClick={handleFilter}>
          Filter
        </Button> */}
        <div className="d-grid gap-2">
          <div className="text-center"> 
            <Button variant="primary" onClick={handleFilter}>
              Filter
            </Button>
          </div>
        </div> 
      </Form>
      <Table striped bordered>
        <thead>
          <tr>
            <th>key_event</th>
            <th>Event Type</th>
            <th>Event Source</th>
            <th>Page</th>
            <th>Fecha</th>
            <th>Hora</th>
          </tr>
        </thead>
        <tbody>
          {limitedEvents.map((event) => (
            <tr key={event.key_event}>
              <td>{event.key_event}</td>
              <td>{event.event_type}</td>
              <td>{event.event_source}</td>
              <td>{event.page}</td>
              <td>{event.fecha}</td>
              <td>{event.hora}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
    
  );
};

export default EventList;
