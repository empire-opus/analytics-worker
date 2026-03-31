// parser.js
import { URL } from 'url';

const parseUrl = (url) => {
  const parsedUrl = new URL(url);
  return {
    protocol: parsedUrl.protocol.replace(':', ''),
    hostname: parsedUrl.hostname,
    pathname: parsedUrl.pathname,
    search: parsedUrl.search,
    hash: parsedUrl.hash,
  };
};

const parseQuery = (search) => {
  const params = {};
  const searchParams = new URLSearchParams(search);
  for (const [key, value] of searchParams) {
    params[key] = value;
  }
  return params;
};

export { parseUrl, parseQuery };