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
    <div className="w-full max-w-full mx-auto p-0 overflow-x-hidden">
      <main className="">
        <section className="bg-white py-16 px-8 mb-12">
          <div className="max-w-[1440px] mx-auto flex flex-col lg:flex-row items-center justify-between gap-16 text-center lg:text-left">
            <div className="flex-1 max-w-xl">
              <h1 className="text-5xl font-extrabold text-[#1a1a1a] mb-6 leading-tight">Premium Phones & Expert Repairs</h1>
              <p className="text-xl text-gray-600 mb-8 leading-relaxed">Shop the latest smartphones or get your device fixed by certified technicians</p>
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
        <div className="products-categories-wrapper">
        <div className="mt-20">
  <section className="w-full mt-8">
    <div className="grid grid-cols-[repeat(auto-fill,_minmax(350px,_1fr))] gap-0">
      {phoneCards.map((card, index) => (
        <Link
          key={index}
          href={card.link}
          className="border-b border-l border-gray-200 text-center py-[10px] px-[40px] w-full pb-[100px] hover:bg-gray-100 cursor-pointer transition-colors duration-100 ease-in"
        >
          <div className="flex flex-col items-center">
            <h2 className="mb-[10px] text-[1.2rem]">{card.name}</h2>
            <button className="bg-transparent border-none text-[#0070f3] cursor-pointer p-0 text-[0.9rem] mb-[10px]">
              View All
            </button>
            <div className="flex justify-center items-center p-[10px]">
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
    <div className="flex items-center gap-0">
      {categoryCards.map((card, index) => (
        <Link
          key={index}
          href={card.link}
          className="border-b border-x border-gray-200 text-center py-[10px] px-[40px] w-full mb-5 pb-[100px] hover:bg-gray-100 cursor-pointer transition-colors duration-100 ease-in"
        >
          <div className="flex flex-col items-center">
            <h2 className="mb-[10px] text-[1.2rem]">{card.name}</h2>
            <button className="bg-transparent border-none text-[#0070f3] cursor-pointer p-0 text-[0.9rem] mb-[10px]">
              View All
            </button>
            <div className="flex justify-center items-center p-[10px]">
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
</div>
        
      </main>
    </div>
  );
}