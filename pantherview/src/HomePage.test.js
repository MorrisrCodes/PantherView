import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import HomePage from './HomePage';

test('search bar is visible and can be typed into', () => {
  render(<HomePage />);

  const input = screen.getByPlaceholderText(/search/i);
  fireEvent.change(input, { target: { value: 'test input' } });

  expect(input.value).toBe('test input');
});