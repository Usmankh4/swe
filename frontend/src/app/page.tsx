import Image from 'next/image';
import Link from 'next/link';

const bannerImage = "/images/phone.png";

const phoneImages: Record<string, string> = {
  apple: "/images/15promax.jpg",
  samsung: "/images/samsungultra.jpg",
  google: "/images/Pixel8.png",
  accessories: "/images/Pixel8.png",
  tablets: "/images/Pixel8.png",
};

export const metadata = {
  title: 'Mobile Repair & Accessories - Your Trusted Tech Partner',
  description: 'Professional phone repair services and premium mobile accessories. We specialize in iPhone, Samsung, and other device repairs.',
};

export default async function Home() {
  const phoneCards = [
    { id: 'apple', name: 'Apple', link: '/brand/Apple', image: phoneImages.apple },
    { id: 'samsung', name: 'Samsung', link: '/brand/Samsung', image: phoneImages.samsung },
    { id: 'android', name: 'Android', link: '/brand/Android', image: phoneImages.google },
  ];

  const categoryCards = [
    { id: 'accessories', name: 'Accessories', link: '/brand/Accessories', image: phoneImages.accessories },
    { id: 'tablets', name: 'Tablets', link: '/brand/Tablet', image: phoneImages.tablets },
  ];

  return (
    <div className="w-full overflow-x-hidden">
      <main>
        {/* HERO SECTION */}
        <section className="bg-white py-16 px-8 mb-12">
          <div className="max-w-[1440px] mx-auto px-4 flex flex-col lg:flex-row items-center justify-between gap-16 text-center lg:text-left">
            <div className="flex-1 max-w-xl">
              <h1 className="text-5xl font-extrabold text-[#1a1a1a] mb-6 leading-tight">Premium Phones & Expert Repairs</h1>
              <p className="text-xl text-gray-600 mb-8 leading-relaxed">
                Shop the latest smartphones or get your device fixed by certified technicians
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start mt-8">
                <Link href="/products/phones" className="btn btn-primary">Shop Phones</Link>
                <Link href="/repair" className="btn btn-outline">Book Repair</Link>
              </div>
            </div>
            <div className="flex-1 flex justify-center items-center mt-8 lg:mt-0">
              <Image
                src={bannerImage}
                alt="Latest Smartphones"
                priority
                width={500}
                height={670}
                className="rounded-xl shadow-xl transition-transform duration-300 ease-in-out animate-[float_6s_ease-in-out_infinite]"
              />
            </div>
          </div>
        </section>

        <div className="max-w-[1440px] mx-auto px-4">
          {/* PHONE CARDS */}
          <section className="w-full mt-8">
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3">
              {phoneCards.map((card, index) => (
                <Link
                  key={index}
                  href={card.link}
                  className="border border-gray-200 text-center py-10 px-6 hover:bg-gray-200 transition-colors duration-150"
                >
                  <div className="flex flex-col items-center">
                    <h2 className="mb-2 text-lg font-semibold">{card.name}</h2>
                    <button className="text-blue-500 text-sm mb-3">View All</button>
                    <div className="p-2">
                      <Image
                        src={card.image}
                        alt={`${card.name} product`}
                        width={243}
                        height={243}
                        style={{ objectFit: 'contain' }}
                      />
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          </section>

          
          <section className="w-full">
            <div className="grid grid-cols-1 sm:grid-cols-2">
              {categoryCards.map((card, index) => (
                <Link
                  key={index}
                  href={card.link}
                  className="border border-gray-200 text-center py-10 px-6 hover:bg-gray-200 transition-colors duration-150"
                >
                  <div className="flex flex-col items-center">
                    <h2 className="mb-2 text-lg font-semibold">{card.name}</h2>
                    <button className="text-blue-500 text-sm mb-3">View All</button>
                    <div className="p-2">
                      <Image
                        src={card.image}
                        alt={`${card.name} category`}
                        width={243}
                        height={243}
                        style={{ objectFit: 'contain' }}
                      />
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          </section>
        </div>
      </main>
    </div>
  );
}
