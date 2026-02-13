import { validateUrl } from '../src/validateUrl';

describe('validateUrl', () => {
  it('should return true for valid URLs', () => {
    expect(validateUrl('http://example.com')).toBe(true);
    expect(validateUrl('https://example.com')).toBe(true);
    expect(validateUrl('http://example.com/path?name=value')).toBe(true);
  });

  it('should return false for invalid URLs', () => {
    expect(validateUrl('htp://example.com')).toBe(false);
    expect(validateUrl('example.com')).toBe(false);
    expect(validateUrl('http://')).toBe(false);
  });
});