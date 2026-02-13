import { validateUrl } from '../src/validateUrl';

describe('validateUrl', () => {
  it('should return true for valid URLs', () => {
    expect(validateUrl('http://example.com')).toBe(true);
    expect(validateUrl('https://example.com')).toBe(true);
    expect(validateUrl('http://www.example.com')).toBe(true);
  });

  it('should return false for invalid URLs', () => {
    expect(validateUrl('example')).toBe(false);
    expect(validateUrl('http://')).toBe(false);
    expect(validateUrl('://example.com')).toBe(false);
  });
});