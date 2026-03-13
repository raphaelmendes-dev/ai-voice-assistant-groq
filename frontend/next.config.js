/** @type {import('next').NextConfig} */
const nextConfig = {
  async redirects() {
    return [
      {
        source: "/",
        destination: "/sofia-voice",
        permanent: false,
      },
    ];
  },
};

module.exports = nextConfig;