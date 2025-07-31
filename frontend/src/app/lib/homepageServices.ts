import { FlashDeal } from './types';

// Mock data for development
const MOCK_FLASH_DEALS: FlashDeal[] = [
  {
    id: '1',
    name: 'Wireless Earbuds Pro',
    slug: 'wireless-earbuds-pro',
    originalPrice: 129.99,
    salePrice: 89.99,
    price: 89.99,
    discount: '30%',
    image: '/products/earbuds.jpg',
    images: [
      { url: '/products/earbuds.jpg', alt: 'Wireless Earbuds Pro' }
    ]
  },
  {
    id: '2',
    name: 'Smart Watch Series 5',
    slug: 'smart-watch-5',
    originalPrice: 299.99,
    salePrice: 229.99,
    price: 229.99,
    discount: '23%',
    image: '/products/smartwatch.jpg',
    images: [
      { url: '/products/smartwatch.jpg', alt: 'Smart Watch Series 5' }
    ]
  },
  {
    id: '3',
    name: 'Bluetooth Speaker',
    slug: 'bluetooth-speaker',
    originalPrice: 79.99,
    salePrice: 49.99,
    price: 49.99,
    discount: '38%',
    image: '/products/speaker.jpg',
    images: [
      { url: '/products/speaker.jpg', alt: 'Bluetooth Speaker' }
    ]
  },
  {
    id: '4',
    name: 'Wireless Charging Pad',
    slug: 'wireless-charger',
    originalPrice: 39.99,
    salePrice: 24.99,
    price: 24.99,
    discount: '38%',
    image: '/products/charger.jpg',
    images: [
      { url: '/products/charger.jpg', alt: 'Wireless Charging Pad' }
    ]
  },
  {
    id: '5',
    name: 'Noise Cancelling Headphones',
    slug: 'noise-cancelling-headphones',
    originalPrice: 199.99,
    salePrice: 149.99,
    price: 149.99,
    discount: '25%',
    image: '/products/headphones.jpg',
    images: [
      { url: '/products/headphones.jpg', alt: 'Noise Cancelling Headphones' }
    ]
  }
];

export async function getFlashDeals(): Promise<FlashDeal[]> {
  // Return mock data for now
  return MOCK_FLASH_DEALS;
  
  // Uncomment this code when backend is ready
  /*
  const res = await fetch('http://127.0.0.1:8000/api/promotions/active-flash-deals/', {
    cache: 'no-store',
  });

  if (!res.ok) {
    throw new Error('Failed to fetch flash deals');
  }

  const rawData: unknown = await res.json();
  const parsed = FlashDealsArraySchema.parse(rawData);

  return parsed.map((p: FlashDealRaw): FlashDeal => ({
    id: p.id,
    name: p.name,
    slug: p.slug,
    originalPrice: parseFloat(p.original_price),
    salePrice: parseFloat(p.sale_price),
    price: parseFloat(p.sale_price),
    discount: p.discount_percentage
      ? `${parseFloat(p.discount_percentage).toFixed(0)}%`
      : 'Sale',
    image: p.image || '/placeholder.jpg',
    images: p.images?.map((img) =>
      typeof img === 'string'
        ? { url: img, alt: p.name }
        : { ...img, alt: img.alt || p.name }
    ) || [{ url: p.image || '/placeholder.jpg', alt: p.name }],
  }));
  */
}
